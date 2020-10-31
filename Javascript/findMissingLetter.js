/*
    Find the missing letter

    Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
    You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
    The array will always contain letters in only one case.

    Example:
    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'

    (Use the English alphabet with 26 letters!)

    Solution:
    1 - iterate the array and comparing the difference between all consecutive items
    2 - when the second item is greater than the first one by more than one
    3 - return the first one plus one
 */

const findMissingLetter = (letters) => {
    let previousLetter = letters[0];
    for(let letter of letters){
        if( letter.charCodeAt(0) - previousLetter.charCodeAt(0) > 1) {
            let missingLetter = previousLetter.charCodeAt(0)+1;
            return String.fromCharCode(missingLetter);
        }
        previousLetter = letter;
    }
    return '';
}
//
// console.log(findMissingLetter(['a','b','c','d','f'])); // e
// console.log(findMissingLetter(['a','b','d','f'])); // c
// console.log(findMissingLetter(['a','c'])); // b
console.log(findMissingLetter(['A','C'])); // B
console.log(findMissingLetter(['A'])); // E
