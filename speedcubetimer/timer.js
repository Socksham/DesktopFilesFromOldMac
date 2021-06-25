function stopWatch(elem){
    var time = 0;
    var interval;
    var offset;

    function update(){
        time += delta();
        var formattedTime = timeFormatter(time);
        elem.textContent = formattedTime;
        //console.log(formattedTime);
    }
    function delta(){
        var now = Date.now();
        var timepassed = now - offset;
        //change or takeout later
        offset = now;
        return timepassed;
    }
    function timeFormatter(timeInMilliseconds){
        var time = new Date(timeInMilliseconds);
        var minutes = time.getMinutes().toString();
        var seconds = time.getSeconds().toString();
        var milliseconds = time.getMilliseconds().toString();

        if(milliseconds.length == 1){
            milliseconds = "00" + milliseconds;
        }else if(milliseconds.length == 2){
            milliseconds = "0" + milliseconds;
        }

        if(minutes == '0'){
            timeWithFormat = seconds + "." + milliseconds;
        }else if(minutes != '0'){
            timeWithFormat = minutes + " : " + seconds + "." + milliseconds;
        }
        //console.log(milliseconds.length);

        return timeWithFormat;

    }
    
    this.isOn = false;
    this.start = function(){
        if(this.isOn == false){
            interval = setInterval(update, 10);
            offset = Date.now();
            this.isOn = true;
        }
    };
    this.stop = function(){
        if(this.isOn == true){
            clearInterval(interval);
            interval = null;
            this.isOn = false;
        }
    };
    this.reset = function(){
        time = 0
    };
}