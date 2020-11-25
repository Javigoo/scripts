function checkScope(){
"use strict";
    var i = "global";
    if(true){
        let i = "local"
        console.log("Local:",i)
    }
    console.log("Global:",i)
}

checkScope();