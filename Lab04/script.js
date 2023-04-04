// show number on id result
var num1 = 0;
var num2 = 0;
var operatorClicked = false;
var decimalClicked = false;
var operator = "";
document.getElementById("result").value = num1;

$(".numbers").click(function() {
    if(operator != "" && operatorClicked == false){
        num1 = 0;
        num2 = 0;
        operator = "";
    }
    if (operatorClicked == false) {
        var num = $(this).val();
        if (num1 == "0") {
            if (num == "." && decimalClicked == false) {
                num1 = "0.";
                document.getElementById("result").value = num1;
                decimalClicked = true;
            } else if(num != ".") {
                num1 = num;
                document.getElementById("result").value = num1;
            }
        }else{
            if (num == "." && decimalClicked == false) {
                num1 = num1 + num;
                document.getElementById("result").value = num1;
                decimalClicked = true;
            } else if (num != ".") {
                num1 = num1 + num;
                document.getElementById("result").value = num1;
            }
    
        }
    } else {
        $(".operator").removeClass("active");
        var num = $(this).val();
        if (num2 == "0") {
            if (num == "." && decimalClicked == false) {
                num2 = "0.";
                document.getElementById("result").value = num2;
                decimalClicked = true;
            } else if (num != ".") {
                num2 = num;
                document.getElementById("result").value = num2;
            }
        } else {
            if (num == "." && decimalClicked == false) {
                num2 = num2 + num;
                document.getElementById("result").value = num2;
                decimalClicked = true;
            } else if (num != ".") {
                num2 = num2 + num;
                document.getElementById("result").value = num2;
            }
        }
    }
});
$(".operator").click(function() {
    if ($(this).val() != "=" ) {
        if (operatorClicked == true && num2 != 0) {
            if(operator == "+"){
                num1 = parseFloat(num1) + parseFloat(num2);
                document.getElementById("result").value = num1;
            }else if(operator == "-"){
                num1 = parseFloat(num1) - parseFloat(num2);
                document.getElementById("result").value = num1;
            }else if(operator == "*"){
                num1 = parseFloat(num1) * parseFloat(num2);
                document.getElementById("result").value = num1;
            }else if(operator == "/"){
                num1 = parseFloat(num1) / parseFloat(num2);
                document.getElementById("result").value = num1;
            }
            operatorClicked = false;
            decimalClicked = false;
        } 
        operatorClicked = true;
        decimalClicked = false;
        operator = $(this).val();
        num2 = "0";
        // console.log(operator); this works for now
        $(this).addClass("active");
        $(".operator").not(this).removeClass("active");
    } 

});

$("#equals").click(function() {
    $(".operator").removeClass("active");
    if (operator != "") {
        if(operator == "+"){
            num1 = parseFloat(num1) + parseFloat(num2);
            document.getElementById("result").value = num1;
        }else if(operator == "-"){
            num1 = parseFloat(num1) - parseFloat(num2);
            document.getElementById("result").value = num1;
        }else if(operator == "*"){
            num1 = parseFloat(num1) * parseFloat(num2);
            document.getElementById("result").value = num1;
        }else if(operator == "/"){
            num1 = parseFloat(num1) / parseFloat(num2);
            document.getElementById("result").value = num1;
        }
        operatorClicked = false;
        decimalClicked = false;
    }
});

$("#clear").click(function() {
    num1 = 0;
    num2 = 0;
    operatorClicked = false;
    decimalClicked = false;
    operator = "";
    document.getElementById("result").value = num1;
    $(".operator").removeClass("active");
});
