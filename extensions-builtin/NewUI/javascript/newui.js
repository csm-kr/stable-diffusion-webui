// // 1. top low 아래 custom 이라 바꾸기 (2023.09.01)
// // top row의 마지막 자식에 

function updateUI(mode) {
    var prefix = mode === 'txt2img' ? 'txt2img' : 'img2img';
    var results = document.getElementById(prefix + '_results');

    // results.style.backgroundImage = url('/workspace/stable-diffusion-webui/outputs/txt2img-images/2023-09-05/00051-596283546.png');

}
const onLoad = (done) => {

    let gradioApp = window.gradioApp;
    updateUI('txt2img');
};

onUiLoaded(onLoad);