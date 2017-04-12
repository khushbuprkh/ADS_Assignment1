$(document).ready(function(){
	$('#filebutton').on('change', ':file', function(){
        var input = $(this);
        label = input.val().replace(/^.*?([^\\\/]*)$/, '$1');
        document.getElementById("packagefile").value = label;
    });

    $(':file').change(function(){
    	if (this.files && this.files[0]){
    		var reader = new FileReader();
    		reader.fileName = this.files[0].name;
    		reader.onload = function(e){
    			if (reader.fileName.indexOf(".json") != -1){
    				var json = JSON.parse(e.target.result);
    				$("#configinput").text(JSON.stringify(json));
    			}
    			else if (reader.fileName.indexOf(".csv") != -1){
    				$("#configinput").text(e.target.result);
    			}
    			else{
    				alert("Only .json and .csv files accepted.");
    				return;
    			}
    		};
    		$("configinput").text(reader.readAsText(this.files[0]));
    	}
    });
    
});