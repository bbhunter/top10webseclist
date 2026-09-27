// Synthetic DOM events exercise the production handlers and animation loop.
// No archive data, browser installation or third-party packages are needed.
import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import {setMaxListeners} from "node:events";
import {test} from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("./constellation.js", import.meta.url), "utf8");

class Element extends EventTarget {
  constructor(tagName = "DIV") {
    super();
    this.tagName = tagName;
    this.dataset = {};
    this.attributes = new Map();
    const classes = new Set();
    this.classList = {
      add: (name) => classes.add(name), remove: (name) => classes.delete(name),
      contains: (name) => classes.has(name),
      toggle: (name, on) => on ? classes.add(name) : classes.delete(name)
    };
    this.style = {setProperty() {}};
  }
  setAttribute(name, value) { this.attributes.set(name, value); }
  getAttribute(name) { return this.attributes.get(name); }
  getBoundingClientRect() { return {left: 0, top: 0, width: 200, height: 200}; }
  setPointerCapture() {}
  focus() {}
}

function fire(target, type, properties = {}) {
  const event = new Event(type, {cancelable: true});
  Object.assign(event, properties);
  target.dispatchEvent(event);
}

function fixture({auto = true, motion = "normal"} = {}) {
  const controls = new Map(["auto", "zoom-in", "zoom-out", "zoom-range"].map((id) =>
    [`#space-${id === "auto" ? "autorotate" : id}`, new Element(id === "zoom-range" ? "DIV" : "BUTTON")]));
  const nav = ["forward", "back", "turn-left"].map((action) => {
    const button = new Element("BUTTON");
    button.dataset.spaceNav = action;
    return button;
  });
  const shell = new Element();
  shell.querySelector = (selector) => controls.get(selector);
  shell.querySelectorAll = () => nav;
  const canvas = new Element("CANVAS");
  canvas.getContext = () => ({setTransform() {}, clearRect() {}});
  const body = new Element("BODY");
  if (motion === "user") body.classList.add("reduce-motion");
  let nextFrame;
  const context = vm.createContext({
    window: {matchMedia: () => ({matches: motion === "system"})},
    document: {body}, AbortController, performance, console,
    requestAnimationFrame: (callback) => { nextFrame = callback; return 1; },
    cancelAnimationFrame() {}
  });
  vm.runInContext(source, context);
  const scene = new context.window.Constellation3D({canvas, shell});
  setMaxListeners(0, scene.signal);
  // Painting is a browser concern; retain the real render clock and loop.
  scene.drawBackdrop = scene.drawScene = () => {};
  scene.setAutoRotate(auto);
  scene.bindEvents();
  scene.loop(100);
  return {scene, canvas, shell, controls, nav, tick: () => nextFrame(scene.lastTime + 16)};
}

const pointer = (pointerId, clientX, clientY) => ({pointerId, clientX, clientY, button: 0});
const actions = [
  ["wheel in", (f) => fire(f.canvas, "wheel", {deltaY: -100})],
  ["wheel out", (f) => fire(f.canvas, "wheel", {deltaY: 100})],
  ...["zoom-in", "zoom-out"].map((id) => [id, (f) => fire(f.controls.get(`#space-${id}`), "click")]),
  ["slider drag", (f) => {
    const slider = f.controls.get("#space-zoom-range");
    fire(slider, "pointerdown", pointer(1, 100, 100));
    fire(slider, "pointermove", pointer(1, 100, 60));
    fire(slider, "pointerup", pointer(1, 100, 60));
    assert.equal(slider.classList.contains("is-active"), false);
  }],
  ...["ArrowUp", "ArrowDown", "PageUp", "PageDown", "Home", "End"].map((key) =>
    [`slider ${key}`, (f) => fire(f.controls.get("#space-zoom-range"), "keydown", {key})]),
  ...["KeyW", "KeyS", "ArrowUp", "ArrowDown"].map((code) => [`camera ${code}`, (f) => {
    fire(f.shell, "keydown", {code}); f.tick(); fire(f.shell, "keyup", {code});
  }]),
  ...["forward", "back"].map((action) => [`navigator ${action}`, (f) => {
    const button = f.nav.find((button) => button.dataset.spaceNav === action);
    fire(button, "pointerdown", pointer(1, 0, 0));
    f.tick();
    fire(button, "pointerup", pointer(1, 0, 0));
  }]),
  ["pinch", (f) => {
    fire(f.canvas, "pointerdown", pointer(1, 50, 100));
    fire(f.canvas, "pointerdown", pointer(2, 150, 100));
    fire(f.canvas, "pointermove", pointer(2, 180, 100));
    fire(f.canvas, "pointerup", pointer(2, 180, 100));
    fire(f.canvas, "pointerup", pointer(1, 50, 100));
    assert.equal(f.scene.pointers.size, 0);
    assert.equal(f.scene.drag, null);
  }]
];

for (const [label, action] of actions) {
  for (const options of [{auto: true}, {auto: false}, {auto: true, motion: "user"}, {auto: true, motion: "system"}]) {
    test(`${label}: preserves drift ${options.auto}, motion ${options.motion || "normal"}`, () => {
      const f = fixture(options);
      const before = f.scene.camera.distance;
      action(f);
      assert.notEqual(f.scene.camera.distance, before, "zoom changes distance");
      assert.equal(f.scene.autoRotate, options.auto, "zoom preserves the chosen drift setting");
      const yaw = f.scene.camera.yaw, visualTime = f.scene.visualTime;
      f.tick();
      const moving = options.auto && !options.motion;
      assert.equal(f.scene.camera.yaw > yaw, moving, "rotation continues only when enabled");
      assert.equal(f.scene.visualTime > visualTime, !options.motion, "animation respects reduced motion");
      assert.equal(f.controls.get("#space-autorotate").getAttribute("aria-pressed"), String(moving));
      assert.equal(f.controls.get("#space-zoom-range").getAttribute("aria-valuenow"), String(Math.round(f.scene.camera.distance)));
      assert.equal(f.shell.dataset.renderError, undefined);
      f.scene.destroy();
    });
  }
  test(`${label}: interrupts a flight so zoom is retained`, () => {
    const f = fixture();
    f.scene.beginFlight({x: 10, y: 0, z: 0}, 140);
    action(f);
    assert.equal(f.scene.flight, null);
    const distance = f.scene.camera.distance;
    f.tick();
    assert.equal(f.scene.camera.distance, distance);
    f.scene.destroy();
  });
}

test("manual orbit still pauses drift", () => {
  const f = fixture();
  fire(f.canvas, "pointerdown", pointer(1, 50, 100));
  fire(f.canvas, "pointermove", pointer(1, 90, 100));
  fire(f.canvas, "pointerup", pointer(1, 90, 100));
  assert.equal(f.scene.autoRotate, false);
  const yaw = f.scene.camera.yaw;
  f.tick();
  assert.equal(f.scene.camera.yaw, yaw);
  f.scene.destroy();
});


test("navigator Play resumes rotation after a mouse drag, and Pause stops it", () => {
  const f = fixture();
  const button = f.controls.get("#space-autorotate");
  fire(f.canvas, "pointerdown", pointer(1, 50, 100));
  fire(f.canvas, "pointermove", pointer(1, 90, 100));
  fire(f.canvas, "pointerup", pointer(1, 90, 100));
  assert.equal(button.textContent, "▶ Play rotation");
  assert.equal(button.getAttribute("aria-label"), "Play rotation");
  const yaw = f.scene.camera.yaw;
  fire(button, "click");
  f.tick();
  assert.ok(f.scene.camera.yaw > yaw);
  assert.equal(button.textContent, "⏸ Pause rotation");
  assert.equal(button.getAttribute("aria-label"), "Pause rotation");
  fire(button, "click");
  const paused = f.scene.camera.yaw;
  f.tick();
  assert.equal(f.scene.camera.yaw, paused);
  assert.equal(button.textContent, "▶ Play rotation");
  assert.equal(button.getAttribute("aria-label"), "Play rotation");
  f.scene.destroy();
});

test("Play interrupts an active camera flight and starts rotation immediately", () => {
  const f = fixture();
  f.scene.beginFlight({x: 10, y: 0, z: 0}, 140);
  const yaw = f.scene.camera.yaw;
  fire(f.controls.get("#space-autorotate"), "click");
  f.tick();
  assert.equal(f.scene.flight, null);
  assert.ok(f.scene.camera.yaw > yaw);
  f.scene.destroy();
});

for (const motion of ["user", "system"]) {
  test(`rotation control respects ${motion} reduced motion`, () => {
    const f = fixture({motion});
    const button = f.controls.get("#space-autorotate");
    assert.equal(button.disabled, true);
    assert.equal(button.textContent, "Rotation paused");
    const yaw = f.scene.camera.yaw;
    fire(button, "click");
    f.tick();
    assert.equal(f.scene.camera.yaw, yaw);
    assert.equal(button.getAttribute("aria-pressed"), "false");
    f.scene.destroy();
  });
}
