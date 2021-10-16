/*
* Left Rotation
* Given a size and a rotation, make the left rotation of an array
* Example:
*
* Input: 5,4 (Array): [1 2 3 4 5]
* Output: [5 1 2 3 4]
*
* [1, 2, 3, 4, 5]
*
* */

const leftRotation = (size, rotation) => {
	const toRotate = Array.from({ length: size }, (_, i) => i+1);
	const rotated  = [];
	
	toRotate.map( (element, i) => {
		const difference = i - rotation;
		const newIndex   = difference >= 0 ? difference : size + difference;
		rotated[newIndex] = element;
	});
	return rotated;
}


console.log(leftRotation(6,3));