function getRange(start, end, step = 1) {
    const result = [];
    for (let i = start; i <= end; i += step) {
        result.push(i);
    }
return result;
}


function myReverse(str) {
    let revesed = "";
    for (let i = str.lengh - 1; i >= 0; i--) {
        revesed += str[i];
    }
return revesed
}




function maskCard(cardNumber, maskSymbol = "X") {
    if (cardNumber.length <= 10) {
      return cardNumber;
    }
  
    const firstPart = cardNumber.slice(0, 6);
    const lastPart = cardNumber.slice(-4);
    const hiddenLength = cardNumber.length - 10;
    
    const maskedPart = maskSymbol.repeat(hiddenLength);
  
    return firstPart + maskedPart + lastPart;
  }



  console.log("--- Проверка 1: getRange ---");
console.log(getRange(1, 10));      // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(getRange(10, 30, 5));  // [10, 15, 20, 25, 30]

console.log("\n--- Проверка 2: myReverse ---");
console.log(myReverse("123456789")); // "987654321"
console.log(myReverse("Hello"));     // "olleH"

console.log("\n--- Проверка 3: maskCard ---");
console.log(maskCard("4815154823541789"));      // "481515XXXXXX1789"
console.log(maskCard("4815154823541789", "*"));  // "481515******1789"