// Wait until the page is loaded
document.addEventListener("DOMContentLoaded", () => {

    const canvas = document.getElementById("introCanvas");

    // If the intro page doesn't exist, stop.
    if (!canvas) return;

    // Create Scene
    const scene = new THREE.Scene();

    // Camera
    const camera = new THREE.PerspectiveCamera(
        60,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );

    camera.position.z = 8;

    // Renderer
    const renderer = new THREE.WebGLRenderer({
        canvas,
        alpha: true,
        antialias: true
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

    // Resize
    window.addEventListener("resize", () => {

        camera.aspect =
            window.innerWidth / window.innerHeight;

        camera.updateProjectionMatrix();

        renderer.setSize(
            window.innerWidth,
            window.innerHeight
        );

    });

    // Animation Loop
    function animate() {

        requestAnimationFrame(animate);

        renderer.render(scene, camera);

    }

    animate();

});