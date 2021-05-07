const clientId = "64a7f9f406c54c02b0200c98943b93dd";
const viewerOptions = {
    embedMode: "LIGHT_BOX",
    defaultViewMode: "FIT_PAGE",
    showDownloadPDF: true,
    showPrintPDF: false
};

function fetchPDF(urlToPDF) {
    return new Promise((resolve) => {
        fetch(urlToPDF)
            .then((resolve) => resolve.blob())
            .then((blob) => {
                resolve(blob.arrayBuffer());
            })
    })
}

function showPDF(urlToPDF) {
    var adobeDCView = new AdobeDC.View({
            clientId: clientId
        });
        var previewFilePromise = adobeDCView.previewFile(
            {
                content: { promise: fetchPDF(urlToPDF) },
                metaData: { fileName: urlToPDF.split("/").slice(-1)[0] }
            },
            viewerOptions
        );
}

document.addEventListener("adobe_dc_view_sdk.ready", function () {
    document.getElementById("showPDF01").addEventListener("click", function () {
        showPDF("https://dl.dropboxusercontent.com/s/3jb1qrfrmxwgvgq/StatementofIntent_AcademicGoals_RachelWang.pdf?dl=0")
    });
    document.getElementById("showPDF02").addEventListener("click", function () {
        showPDF("https://dl.dropboxusercontent.com/s/8ya3urr4mxtgyue/QDG_Notes_RachelWang.pdf?dl=0")
    });
    document.getElementById("showPDF03").addEventListener("click", function () {
        showPDF("https://dl.dropboxusercontent.com/s/3jslattisxo78h8/MLOOpaper_RachelWang.pdf?dl=0")
    });
});

// Add arrayBuffer if necessary i.e. Safari
(function () {
    if (Blob.arrayBuffer != "function") {
        Blob.prototype.arrayBuffer = myArrayBuffer;
    }

    function myArrayBuffer() {
        return new Promise((resolve) => {
            let fileReader = new FileReader();
            fileReader.onload = () => {
                resolve(fileReader.result);
            };
            fileReader.readAsArrayBuffer(this);
        });
    }
})();


// use cookies to check if it is the user's first time

$('document').ready(function(){
    if ($.cookie('has_visited') != TRUE){
       $('#ele_id').trigger('click');
       $.cookie('has_visited', TRUE, { expires: 1 }); //this will set the cookie to expire after one day but you could make it longer
   });
