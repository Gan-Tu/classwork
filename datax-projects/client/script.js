// Globals.
var urlFormId = '#url-form';
var urlFormInputId = '#url-form-input';
var videoIFrameId = '#video-iframe';
var labelsListId = '#labels-list';
var initialVideoURL = 'https://www.youtube.com/watch?v=JphHw6iU4m8';
var availableListLeftID = '#available-list-left'
var availableListRightID = '#available-list-right'
var colors = ['red', 'orange', 'green', 'blue', 'purple'];


function setVideoTime(seconds) {
    var iframe = $(videoIFrameId);
    var currentSrc = iframe.attr('src');
    var newSrc = currentSrc.split('?').shift();
    newSrc += "?start=" + seconds + "&autoplay=1";
    iframe.attr('src', newSrc);
    iframe.contentWindow.location.reload();
    return false; // Prevents page reload
}

function secondsToHms(d) {
    d = Number(d);
    var h = Math.floor(d / 3600);
    var m = Math.floor(d % 3600 / 60);
    var s = Math.floor(d % 3600 % 60);
    return ((h > 0 ? h + ":" + (m < 10 ? "0" : "") : "") + m + ":" + (s < 10 ? "0" : "") + s);
}

function loadVideo(id) {
    var urlFormInput = $(urlFormInputId);
    urlFormInput.val('http://youtu.be/' + id);
    urlFormInput.submit();
}

$(document).ready(function() {

    var urlForm = $(urlFormId);
    var urlFormInput = $(urlFormInputId);
    var videoIFrame = $(videoIFrameId);
    var labelsList = $(labelsListId);
    var availableListIdLeft = $(availableListLeftID)
    var availableListIdRight = $(availableListRightID)

    // Ask for cached section stuff
    axios.get('/cached')
        .then(function (response) {
            data = response.data
            var thumbs = data.slice(0, data.length / 2 + 1).map(function(id) {
               return '<li style="padding-top:20px"><a onclick="loadVideo(\'' + id + '\')"'
                 + 'href="javascript:void(0)"> '
                 + '<img src="http://img.youtube.com/vi/' + id + '/1.jpg" '
                 + 'height="90" width="120"> </a></li>';
            }).join('');
            availableListIdLeft.html('<div class="col-md-2">' + thumbs + '</div>')
            var thumbs_right = data.slice(data.length / 2).map(function(id) {
               return '<li style="padding-top:20px"><a onclick="loadVideo(\'' + id + '\')"'
                 + 'href="javascript:void(0)"> '
                 + '<img src="http://img.youtube.com/vi/' + id + '/1.jpg" '
                 + 'height="90" width="120"> </a></li>';
            }).join('');
            availableListIdRight.html('<div class="col-md-2">' + thumbs_right + '</div>')
        });

    // Set up submit Handler
    urlForm.submit(function urlFormSubmit(event) {
        labelsList.html('<p>Loading, this may take some time depending on the video length.</p>')
        // Don't reload the page.
        event.preventDefault();

        // Set the video URL
        // User gives: https://www.youtube.com/watch?v=YbcxU1IK7s4
        // Embed frame needs: https://www.youtube.com/embed/YbcxU1IK7s4
        var url = urlFormInput.val()
        var videoId = url.split("v=").length == 2 ? url.split("v=").pop() : url.split('/').pop()

        var embedURL = 'https://www.youtube.com/embed/' + videoId;
        videoIFrame.attr('src', embedURL);

        // Define the request
        var reqBody = {
            url: urlFormInput.val()
        };

        // Post the request
        axios.post('/video', reqBody)
            .then(function responseHandler(response) {
                var displayLabels;
                if (response.data.hasOwnProperty('sortedLabels')) {
                    displayLabels = response.data.sortedLabels.slice(0, 20); // {0 : "label"}
                }
                else {
                    alert("Response wasn't good");
                    console.log(response.data);
                }
                var listItems = [];
                var label;
                var info;;
                for(var i in displayLabels) {
                    label = displayLabels[i];
                    info = response.data.labels[label];
                    // Create the links for each list item.
                    var timeLinks = info.times.map(function(time) {
                        var hms = secondsToHms(time);
                        return '<a class="" onclick="setVideoTime(' + time + ')" href="javascript:void(0)">' +
                            hms + '</a>';
                    });
                    // Capitalize the first letter.
                    label = _.upperFirst(label);
                    var toAdd = '';
                    if (i % 5 == 0) {
                        toAdd += '<div class="col-md-2 col-md-offset-1" style="height:350px;"><h5 style="background-color:' + colors[i % 5] + '; padding: 2px; margin: 0 auto; color: white">' + label + '</h5><div style="overflow-y: scroll; height: 80%; margin-top:5%;"><ul class="list-unstyled">';
                    } else {
                        toAdd += '<div class="col-md-2" style="height:350px;"><h5 style="background-color:' + colors[i % 5] + '; padding: 2px;  margin: 0 auto; color: white">' + label + '</h5><div style="overflow-y: scroll; height: 80%; margin-top:5%;"><ul class="list-unstyled">';
                    }
                    
                    for (var j in timeLinks) {
                        toAdd += '<li>' + timeLinks[j] + '</li>';
                    }
                    toAdd += '</ul></div></div>';

                    listItems.push(toAdd);
                }

                // Insert the list items.
                labelsList.html(listItems);
            });

    });

    // Send an initial fake request.
    urlFormInput.val(initialVideoURL);
    urlForm.submit();
});
