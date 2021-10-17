/*
* Return to n prime number sequence by given a number.
* A prime number or a prime is a natural number greater than 1
* And can be divisible only by 1 and by itself.
* Example:
*
* Input: 5
* Output: 2,3,5,7,11
*
* */


const isPrime = (number) => {
	if(number <= 1) return false;
	let dividers = 0;
	
	for(let i = 1; i <= number; i++){
		if(dividers > 2) return false;
		if( number%i === 0 ) dividers++;
	}
	
	return dividers === 2;
};

const nPrime = (n) => {
	if(n <= 0) throw new Error('The n parameter must be a positive number greater than 0')
	
	const primes = [];
	let i = 1;
	
	while(primes.length !== n){
		if(isPrime(i)) primes.push(i);
		i++;
	}
	return primes;
}

console.log(nPrime(-10))






