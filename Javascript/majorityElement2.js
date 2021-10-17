/*
* Majority Element 2 (Medium level)
* Given an integer array of size n, find all elements that appear more than [ n /3 ] times.
*
* Example:
* Input: [3,2,3]
* Output: [3]
*
* Input: [1,2]
* Output: [1,2]
*
* */

const majorityElement2 = (nums) => {
	
	const countElements = {};
	const majorityElements = [];
	const constrain = nums.length / 3;
	
	nums.forEach( key => countElements[key] ? countElements[key]++ : countElements[key] = 1);
	
	Object.keys(countElements).forEach( key => {
		countElements[key] > constrain ? majorityElements.push(key) : 0;
	});
	
	return majorityElements;
};


console.log(majorityElement2([3,2,3])); // [3]
console.log(majorityElement2([1,2])); // [1,2]