/*
* Majority Element
*
* Given an array of nums of size n, return the majority element.
*
* The majority element is the element that appears more than [ n / 2] times.
* You may assume that the majority element always exists in the array.
*
* Example:
*
* input: [ 3,2,3 ]
* output: 3
* */


const majorityElement = (nums) => {
	const countElements = {};
	let majorityElement = 0;
	
	nums.map( element => {
		if(countElements[element]) countElements[element]++;
		else countElements[element] = 1;
	});
	
	Object.keys(countElements).forEach( (key) => {
		if(countElements[key] > nums.length / 2){
			majorityElement = key;
		}
	});
	
	return majorityElement;
}


console.log(majorityElement([3,2,3]))

