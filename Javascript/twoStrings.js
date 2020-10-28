/*
*   Two Strings
*   Write a function that given two strings return if the first one shares a substring with second one
*   returning 'YES' or 'NO'
*   Example:
*   Input: "hellllllllllllllllllo" , "xwdto" O(M*N)
*   Output: "NO"
* */

const holaMundo = () => {
    console.log("hola mundo");
}

const twoStrings = (stringOne, stringTwo) => {
    if(
        (!stringOne || !stringTwo) ||
        (typeof stringOne !== 'string' || typeof stringTwo !== 'string')
    )
        return 'NO';

    const stringOneSet = new Set(stringOne.split(''));
    const stringTwoSet = new Set(stringTwo.split(''));
    let result = 'NO'

    stringOneSet.forEach((c) => {
        stringTwoSet.forEach((sc) => {
            if(c === sc)
                result = 'YES';
        });
    });

    return result;
}

console.log(twoStrings("hola", "crayola")); // YES
console.log(twoStrings("", "crayola")); // NO
console.log(twoStrings("hola", "cici")); // NO
console.log(twoStrings(undefined, "crayola")); // NO
console.log(twoStrings(null, "crayola")); // NO
//console.log(twoStrings(holaMundo, "tasdl"));
//console.log(twoStrings(holaMundo, holaMundo));