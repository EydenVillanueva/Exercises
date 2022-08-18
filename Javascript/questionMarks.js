const QuestionsMarks = (str) => {
	const sentence = str.match(/[0-9?]/g);
	
	let questionCounter = 0;
	let number = 0;
	let response = false;
	
	for(let i = 0; i < sentence.length; i++){
		if(sentence[i] === '?' && number){
			questionCounter++;
		}
		else {
			if(questionCounter === 3 && number) {
				response = Number(sentence[i]) + number === 10;
				number = 0
				questionCounter = 0;
			}
			else {
				number = !isNaN(sentence[i])&& Number(sentence[i]);
			}
		}
	}
	
	return response;
};

// keep this function call here
console.log(QuestionsMarks("9???1???9??1???9")); //false
console.log(QuestionsMarks("5??a?5?5")); //true
console.log(QuestionsMarks("aa6?9")); //false
console.log(QuestionsMarks("7???3r1??????5")); //true
console.log(QuestionsMarks("arrb6???4xxbl5???eee5")); //true

