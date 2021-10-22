// quiz([11, 9, 6, 11, 5], 3); 	// output: 26, 16 // 5 3
// quiz([11, 9, 6, 11, 5, 1], 3);	// output: 26, 17
// quiz([11, 9, 6, 11, 5, 1, 1], 3); 	// output: 26, 17, 1

// quiz sums every n elements of arr and print.
// also print the sum of any remaining elements

const quiz = (arr, n) => {
	let count = 0;
	let arrayCount = 0;
	let currenSum = 0;
	
	arr.map(element => {
		count += 1;
		arrayCount += 1;
		currenSum += element;
		
		if(arrayCount === arr.length) {
			console.log(currenSum);
			return currenSum;
		}
		
		if(count === n){
			count = 0;
			console.log(currenSum)
			currenSum = 0;
		}
	});
}

console.log(quiz([11], 5)); // 20