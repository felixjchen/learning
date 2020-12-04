var peer = new Peer();
// var options = {
//     'host': '127.0.0.1',
//     'port': 9000,
//     'path': '/myapp'
// }
// var peer = new Peer(uuidv4(), options);

var screenStream = null

var emptyAudioTrack = null;
var emptyVideoTrack = null;
var emptyMediaStream = null;

var video = null
$(function () {
    video = document.getElementById("media")
});

peer.on('open', function (id) {
    console.log('My peer ID is: ' + id);
    $('#clientID').text('My peer ID is: ' + id);
});

peer.on('call', function (call) {
    call.answer(screenStream);
});

//  Actions
function getScreenStream(peerID) {
    // Connect with empty media stream
    if (emptyMediaStream == null) {
        emptyAudioTrack = createEmptyAudioTrack();
        emptyVideoTrack = createEmptyVideoTrack({
            width: 1920,
            height: 1080
        });
        emptyMediaStream = new MediaStream([emptyAudioTrack, emptyVideoTrack])
    }

    call = peer.call(peerID, emptyMediaStream);
    call.on('stream', function (stream) {
        console.log('Got stream ', stream)
        video.srcObject = stream
        video.muted = false
        video.controls = true
    });
}


// Helpers
function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        let r = Math.random() * 16 | 0,
            v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function createEmptyAudioTrack() {
    let ctx = new AudioContext();
    let oscillator = ctx.createOscillator();
    let dst = oscillator.connect(ctx.createMediaStreamDestination());
    oscillator.start();
    let track = dst.stream.getAudioTracks()[0];
    return Object.assign(track, {
        enabled: false
    });
};

function createEmptyVideoTrack({
    width,
    height
}) {
    let canvas = Object.assign(document.createElement('canvas'), {
        width,
        height
    });
    canvas.getContext('2d').fillRect(0, 0, width, height);

    let stream = canvas.captureStream();
    let track = stream.getVideoTracks()[0];

    return Object.assign(track, {
        enabled: false
    });
};

function setScreenStream() {
    let options = {
        video: {
            width: 1920,
            height: 1080,
            frameRate: 60
        },
        audio: {
            autoGainControl: false,
            googAutoGainControl: false,
            echoCancellation: false,
            noiseSuppression: false,
            sampleRate: 44100
        }
    }
    navigator.mediaDevices.getDisplayMedia(options).then(function (stream) {
            console.log('Created display media', stream)
            screenStream = stream
        })
        .catch(function (err) {
            console.log("Error when calling with screen media stream")
        });
}