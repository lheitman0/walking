// Basic Three.js setup
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
camera.position.z = 5;

const cardElements = document.querySelectorAll('.card');
cardElements.forEach((card, index) => {
  const geometry = new THREE.PlaneGeometry(1, 1.5);
  const uniforms = {
    u_time: { type: "f", value: 1.0 },
    u_resolution: { type: "v2", value: new THREE.Vector2() },
    u_image: { type: "t", value: new THREE.TextureLoader().load(card.querySelector('img').src) }
  };

  const shaderMaterial = new THREE.ShaderMaterial({
    uniforms: uniforms,
    vertexShader: vertexShaderCode,
    fragmentShader: fragmentShaderCode
  });

  const plane = new THREE.Mesh(geometry, shaderMaterial);
  plane.position.x = (index % 3) - 1; // Adjust positioning based on index
  plane.position.y = Math.floor(index / 3) - 1;
  scene.add(plane);

  card.addEventListener('mouseover', () => {
    uniforms.u_time.value += 0.5;
  });

  card.addEventListener('mouseout', () => {
    uniforms.u_time.value -= 0.5;
  });
});

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

animate();

const vertexShaderCode = `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const fragmentShaderCode = `
  uniform float u_time;
  uniform vec2 u_resolution;
  uniform sampler2D u_image;
  varying vec2 vUv;
  
  void main() {
    vec2 uv = vUv;
    uv.y += sin(uv.x * 10.0 + u_time) * 0.1;
    gl_FragColor = texture2D(u_image, uv);
  }
`;
