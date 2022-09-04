const inputFile = document.getElementById('foto');
const previewContainer = document.getElementById('preview');
const previewImage = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");

inputFile.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
        const reader = new FileReader();

        previewDefaultText.style.display="none";
        previewImage.style.display="block";


        reader.addEventListener("load", function(){
            previewImage.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }else{
        previewDefaultText.style.display=null;
        previewImage.style.display=null;
        previewImage.setAttribute("src", "");
    }
});