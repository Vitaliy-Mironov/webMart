window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 800 || document.documentElement.scrollTop > 800) {
        document.getElementById("upBtn").style.display = "flex";
    } else {
        document.getElementById("upBtn").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

// function minusProduct(idCounter) {
//     if (document.getElementById(idCounter).textContent != '1') {
//         let counter = document.getElementById(idCounter).textContent;
//         document.getElementById(idCounter).textContent = (Number(counter) - 1);
//     }
// }

// function plusProduct(idCounter) {
//     let counter = document.getElementById(idCounter).textContent;
//     document.getElementById(idCounter).textContent = (Number(counter) + 1);
// }

function copyrightYears() {
    var start_year = 2023;  // поменять на год начала работы сайта
    var this_year = new Date().getFullYear();
    if (start_year < this_year) {document.write(start_year + '-' + this_year);}
    else {document.write(this_year);}
}

// function generatePassword(idGenPass) {
//     var length = 8,
//         symbols = "23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz!@#%&$",
//         result = "";
//     for (var i = 0, n = symbols.length; i < length; ++i) {
//         result += symbols.charAt(Math.floor(Math.random() * n));
//     }
//     document.getElementById(idGenPass).value = result;
// }
