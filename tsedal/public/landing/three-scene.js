/**
 * TSEDAL (ጸዳል) LMS — KINETIC LIGHT WAVE
 * Ambient, mathematical undulating light plane in the background
 */

(function () {
  'use strict';

  const canvas = document.getElementById('kineticWaveCanvas');
  const container = document.querySelector('.canvas-ambient-stage');

  if (!canvas || !container || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  if (typeof THREE === 'undefined') {
    init2DFallback(canvas, container);
    return;
  }

  let scene, camera, renderer;
  let waveMesh;
  let width, height;
  let mouse = { x: 0, y: 0, targetX: 0, targetY: 0 };
  let clock = new THREE.Clock();
  let isVisible = true;

  const COLS = 54;
  const ROWS = 38;
  const WIDTH = 260;
  const HEIGHT = 180;

  function init() {
    width = container.clientWidth || window.innerWidth;
    height = container.clientHeight || window.innerHeight;

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x070e22, 0.004);

    camera = new THREE.PerspectiveCamera(45, width / height, 1, 1000);
    camera.position.set(0, -30, 110);
    camera.lookAt(0, 15, 0);

    renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance'
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    const geometry = new THREE.PlaneGeometry(WIDTH, HEIGHT, COLS - 1, ROWS - 1);
    const material = new THREE.MeshBasicMaterial({
      color: 0x00f0ff,
      wireframe: true,
      transparent: true,
      opacity: 0.16,
      blending: THREE.AdditiveBlending
    });

    waveMesh = new THREE.Mesh(geometry, material);
    waveMesh.rotation.x = -Math.PI / 2.5;
    waveMesh.position.y = -15;
    scene.add(waveMesh);

    window.addEventListener('resize', onResize, { passive: true });
    window.addEventListener('mousemove', onMouseMove, { passive: true });

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((e) => { isVisible = e.isIntersecting; });
      }, { threshold: 0.05 });
      observer.observe(container);
    }

    animate();
  }

  function onResize() {
    width = container.clientWidth || window.innerWidth;
    height = container.clientHeight || window.innerHeight;

    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  function onMouseMove(e) {
    const nx = (e.clientX / window.innerWidth) * 2 - 1;
    const ny = -(e.clientY / window.innerHeight) * 2 + 1;
    mouse.targetX = nx * 8;
    mouse.targetY = ny * 5;
  }

  function animate() {
    requestAnimationFrame(animate);

    if (!isVisible || document.hidden) return;

    const t = clock.getElapsedTime() * 0.7;

    mouse.x += (mouse.targetX - mouse.x) * 0.04;
    mouse.y += (mouse.targetY - mouse.y) * 0.04;

    camera.position.x = mouse.x * 0.5;
    camera.position.y = -30 + mouse.y * 0.4;
    camera.lookAt(0, 15, 0);

    const pos = waveMesh.geometry.attributes.position;
    const count = pos.count;

    for (let i = 0; i < count; i++) {
      const u = (i % COLS) / COLS;
      const v = Math.floor(i / COLS) / ROWS;

      const z = Math.sin(u * 6.0 + t) * 4.2 +
                Math.cos(v * 5.0 + t * 0.8) * 3.6 +
                Math.sin((u + v) * 4.0 - t * 1.1) * 2.8;

      pos.setZ(i, z);
    }

    pos.needsUpdate = true;
    renderer.render(scene, camera);
  }

  function init2DFallback(cvs, cnt) {
    const ctx = cvs.getContext('2d');
    if (!ctx) return;
    let w, h;
    let t = 0;

    function resize() {
      w = cvs.width = cnt.clientWidth || window.innerWidth;
      h = cvs.height = cnt.clientHeight || window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    function draw() {
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = 'rgba(0, 240, 255, 0.12)';
      ctx.lineWidth = 1;

      for (let i = 0; i < 14; i++) {
        ctx.beginPath();
        const yBase = h * 0.6 + i * 10;
        for (let x = 0; x < w; x += 15) {
          const y = yBase + Math.sin(x * 0.01 + t + i * 0.2) * 14;
          if (x === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }
      t += 0.015;
      requestAnimationFrame(draw);
    }
    draw();
  }

  function initializeSafely() {
    try {
      init();
    } catch (_) {
      // WebGL may be unavailable; a new canvas can acquire a 2D context.
      const fallbackCanvas = canvas.cloneNode();
      canvas.replaceWith(fallbackCanvas);
      init2DFallback(fallbackCanvas, container);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeSafely);
  } else {
    initializeSafely();
  }
})();
