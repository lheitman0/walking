import streamlit as st
import os
from pathlib import Path
import base64

# Page configuration
st.set_page_config(
    page_title="Walk More",
    page_icon="🚶",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to replicate the Django app styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Chomsky&display=swap');

.stMain {
    background-color: #080808;
}

.stApp {
    background-color: #080808;
}

.main .block-container {
    background-color: #080808;
    color: white;
}

h1, h2, h3, p, label, input, li {
    font-family: 'Chomsky', Arial, sans-serif;
    color: white;
}

.stButton > button {
    background-color: black;
    color: white;
    border: 1px solid white;
    border-radius: 5px;
    font-family: 'Chomsky', Arial, sans-serif;
    font-size: 18px;
    padding: 15px 30px;
    margin: 20px 0;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: white;
    color: black;
    transform: scale(1.05);
}

.info-card {
    background-color: rgba(0, 0, 0, 0.7);
    border: 1px solid white;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    transition: transform 0.3s ease;
    text-align: center;
    height: 500px;
    display: flex;
    flex-direction: column;
}

.info-card:hover {
    transform: scale(1.05);
}

.info-card img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    border-radius: 5px;
    margin-bottom: 15px;
    flex-grow: 1;
}

.info-card a {
    color: white;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.info-card a:hover {
    color: #cccccc;
}

.info-card h3 {
    margin: 10px 0;
    font-size: 1.2em;
    flex-shrink: 0;
}

.main-message {
    text-align: center;
    font-size: 2.5em;
    line-height: 1.4;
    margin: 50px 0;
    padding: 0 20px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
    max-width: 800px;
    z-index: 10;
}

.title-text {
    text-align: center;
    font-size: 3.5em;
    font-weight: bold;
    margin: 50px 0;
    position: absolute;
    top: 10%;
    left: 50%;
    transform: translateX(-50%);
    width: 100%;
    z-index: 10;
}

.read-button-container {
    position: absolute;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    z-index: 10;
}

.canvas-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.text-overlay {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-family: 'Chomsky', Arial, sans-serif;
    font-size: 55px;
    font-weight: bold;
    text-align: center;
    z-index: 2;
}

.read-button {
    position: fixed;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    background-color: transparent;
    border: 1px solid white;
    color: white;
    font-family: 'Chomsky', Arial, sans-serif;
    font-size: 18px;
    padding: 15px 30px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
    text-decoration: none;
}

.read-button:hover {
    background-color: white;
    color: #080808;
}
</style>
""", unsafe_allow_html=True)

def get_image_base64(image_path):
    """Convert image to base64 for embedding in HTML"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Navigation
    if st.session_state.page == 'home':
        show_home_page()
    elif st.session_state.page == 'info':
        show_info_page()

def show_home_page():
    """Display the home page with the message and Lorenz attractor animation"""
    
    # Create a container for the background animation
    st.markdown("""
    <div class="canvas-container">
        <canvas id="lorenz-canvas"></canvas>
    </div>
    """, unsafe_allow_html=True)
    
    # Add JavaScript for the Lorenz attractor
    st.markdown("""
    <script type="importmap">
    {
        "imports": {
        "three": "https://unpkg.com/three@0.122.0/build/three.module.js",
        "three/addons/": "https://unpkg.com/three@0.122.0/examples/jsm/"
        }
    }
    </script>
    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

        let camera, controls, scene, renderer, pc, group, mouse, raycaster;

        // initial conditions hand-picked to look nice
        var a_0 = 1.062477352437103;
        var b_0 = 8.038291607940321;
        var f_0 = 15.4135763998;
        var g_0 = 1.8347793740599485;

        init();
        timeskip(a_0, b_0, f_0, g_0);
        render(a_0, b_0, f_0, g_0);

        function init() {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera( 100, window.innerWidth / window.innerHeight, 0.1, 50 );
            camera.position.z = 30;

            renderer = new THREE.WebGLRenderer( { antialias: true } );
            renderer.setPixelRatio( window.devicePixelRatio );
            renderer.setSize( window.innerWidth, window.innerHeight);
            renderer.setClearColor( 0x080808, 1 );
            document.getElementById('lorenz-canvas').appendChild( renderer.domElement );

            group = new THREE.Group();

            controls = new OrbitControls( camera, renderer.domElement );
            controls.enableDamping = true;
            controls.dampingFactor = 0.25;
            controls.screenSpacePanning = false;
            controls.minDistance = 0.1;
            controls.maxDistance = 50;
            controls.maxPolarAngle = Math.PI / 2;
            controls.enableZoom = false;

            var arrayCurve = lorenz(a_0, b_0, f_0, g_0);
            var curve = new THREE.CatmullRomCurve3(arrayCurve);
            var geometry = new THREE.Geometry();
            geometry.vertices = curve.getPoints(111111);

            // points to apply to the geometry defined by the curve
            var pcMat = new THREE.PointsMaterial();
            pcMat.color = new THREE.Color(0x967bb6);
            pcMat.transparent = true;
            pcMat.size = 0.01;
            pcMat.blending = THREE.AdditiveBlending;
            pc = new THREE.Points(geometry, pcMat);
            pc.sizeAttenuation = false;
            pc.sortPoints = true;

            group.add(pc);
            scene.add( group );

            mouse = new THREE.Vector2();
            raycaster = new THREE.Raycaster();

            window.addEventListener( 'mousemove', onMouseMove, false );
        }

        function onMouseMove( event ) {
            mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
            mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
        }

        function render(a_0, b_0, f_0, g_0) {
            requestAnimationFrame( function() { render(a_0, b_0, f_0, g_0) } );
            controls.update();
            renderer.render( scene, camera );

            // trying to add interactivity
            raycaster.setFromCamera( mouse, camera );
            // calculate objects intersecting the picking ray
            var intersects = raycaster.intersectObject( pc );
            for ( var i = 0; i < intersects.length; i++ ) {
                intersects[i].point.sub( mouse ).multiplyScalar(5);
            }

            pc.geometry.colorsNeedUpdate = true;

            // randomly varying the initial parameters of the lorenz attractor
            var geometry = pc.geometry;
            var a = a_0+Math.random()*6;
            var b = b_0+Math.random()*7;
            var x_drift = (f_0+Math.random()*8)*a;
            var y_drift = g_0+Math.random();
            var dt = 0.0002;

            geometry.vertices.forEach(function(v){
                v.x = v.x + dt*(-a*v.x + v.y*v.y   - v.z*v.z   + x_drift);
                v.y = v.y + dt*(-v.y   +  v.x*v.y  - b*v.x*v.z + y_drift);
                v.z = v.z + dt*(-v.z   + b*v.x*v.y + v.x*v.z);
            })

            geometry.verticesNeedUpdate = true;
            group.rotation.x += 0.001;
            group.rotation.y += 0.002;
            group.rotation.z -= 0.001;

            window.addEventListener( 'resize', function () {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize( window.innerWidth, window.innerHeight );
            }, false );
        }

        // initialize the lorenz attractor
        function lorenz(a, b, x_drift, y_drift){
            var arrayCurve=[];
            var x = 0.01;
            var y = 0.01;
            var z = 0.01;
            var dt = 0.001;

            for (var i=0;i<100000;i++){
                x = x - dt*(a*x + y*y   - z*z   + x_drift);
                y = y - dt*(y   + x*y   - b*x*z + y_drift);
                z = z - dt*(z   + b*x*y + x*z);
                arrayCurve.push(new THREE.Vector3(x, y, z).multiplyScalar(1));
            }
            return arrayCurve;
        }

        // progress through the animation a bit to get to the good stuff
        function timeskip(){
            var geometry = pc.geometry;
            var a       = 3.664669162451547;
            var b       = 5.508898472476083;
            var x_drift = 46.515675857312345;
            var y_drift = 2.8005228465422123;
            var dt      = 0.0057;

            for (var i=0;i<100;i++) {
                geometry.vertices.forEach(function(v){
                    v.x = v.x + dt*(-a*v.x + v.y*v.y   - v.z*v.z   + x_drift);
                    v.y = v.y + dt*(-v.y   +  v.x*v.y  - b*v.x*v.z + y_drift);
                    v.z = v.z + dt*(-v.z   + b*v.x*v.y + v.x*v.z);
                })

                geometry.verticesNeedUpdate = true;
                group.rotation.x += 0.01;
                group.rotation.y += 0.02;
                group.rotation.z -= 0.01;
            }
        }
    </script>
    """, unsafe_allow_html=True)
    
    # Title at the top
    st.markdown("""
    <div style="text-align: center; font-size: 2.5em; margin: 50px 0; font-weight: normal;">Walk More</div>
    """, unsafe_allow_html=True)
    
    # Main message in the middle
    st.markdown("""
    <div style="text-align: center; font-size: 1.8em; line-height: 1.4; padding: 0 20px; margin: 100px 0; font-weight: normal;">
        Please walk more. I'm begging you. A long aimless walk with no headphones will solve your problems I promise. What do you find when you only look for yourself?
    </div>
    """, unsafe_allow_html=True)
    
    # Read button in a separate container
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Read", key="read_btn", use_container_width=True):
            st.session_state.page = 'info'
            st.rerun()

def show_info_page():
    """Display the info page with the cards"""
    st.markdown("<h1 style='text-align: center; font-size: 2.5em; margin-bottom: 30px;'>Read</h1>", unsafe_allow_html=True)
    
    # Get the image paths from the items directory
    items_dir = Path("items")
    nietzsche_img = items_dir / "edgedancer.jpeg"
    other_img = items_dir / "original_0f77776a3f1293bf49690974cbec7d2d.jpeg"
    
    # Convert images to base64
    nietzsche_base64 = get_image_base64(nietzsche_img)
    other_base64 = get_image_base64(other_img)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if nietzsche_base64:
            st.markdown(f"""
            <div class="info-card">
                <a href="https://im1776.com/2022/10/28/walking-with-nietzsche/" target="_blank">
                    <img src="data:image/jpeg;base64,{nietzsche_base64}" alt="Walking With Nietzsche">
                    <h3>Walking With Nietzsche By Riva Melissa-Tez</h3>
                </a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-card">
                <a href="https://im1776.com/2022/10/28/walking-with-nietzsche/" target="_blank">
                    <h3>Walking With Nietzsche By Riva Melissa-Tez</h3>
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if other_base64:
            st.markdown(f"""
            <div class="info-card">
                <a href="https://psycnet.apa.org/record/2014-14435-001" target="_blank">
                    <img src="data:image/jpeg;base64,{other_base64}" alt="Give your ideas some legs">
                    <h3>Give your ideas some legs: The positive effect of walking on</h3>
                </a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="info-card">
                <a href="https://psycnet.apa.org/record/2014-14435-001" target="_blank">
                    <h3>Give your ideas some legs: The positive effect of walking on</h3>
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("Back to Home"):
        st.session_state.page = 'home'
        st.rerun()

if __name__ == "__main__":
    main() 