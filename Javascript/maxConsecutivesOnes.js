/*
*   Given an array of positive and negative numbers
*   return count of all the consecutive 1 of the array.
*   Example:
*   Input: [1,0,-3,1,1]
*   Output: 2
* */

const consecutiveOnes = (numbers) => {
    let maxConsecutive = 0;
    let mConsecutive = 0;

    numbers.forEach((number) => {
        if(number === 1) {
            mConsecutive++;
        }
        else {
            if (mConsecutive > maxConsecutive) {
                maxConsecutive = mConsecutive;
            }
            mConsecutive = 0;
        }
    });

    return maxConsecutive;
}

console.log(consecutiveOnes([0,2,4,1,3,1,1,3,0,10,-2,-3,1])); // 2
console.log(consecutiveOnes([1,1,1,1,3,1,1,3,0,10,-2,-3,1])); // 4
console.log(consecutiveOnes([0,2,4,0,3,0,0,3,0,10,-2,-3,0])); // 0
console.log(consecutiveOnes([undefined, 1, undefined, null, NaN])); // 1
console.log(consecutiveOnes(["string", -4, 4])); // 0