const b1 = document.querySelectorAll ('button')[0];
b1.addEventListener('click',function () {
    var audio = new Audio ('sound/accent.mp3')
    audio.play();
})
const b2 = document.querySelectorAll ('button')[1];
b2.addEventListener('click', function (){
    var audio1 = new Audio ('sound/mixkit.wav');
    audio1.play();
})

const b3 = document.querySelectorAll ('button')[2];
b3.addEventListener('click', function(){
    var audio2 = new Audio ('sound/strom.mp3')
    audio2.play();
})

const b4 = document.querySelectorAll ('button')[3];
b4.addEventListener('click', function(){
    var audio3 = new Audio ('sound/whoosh.mp3');
    audio3.play();
})

