console.log("hello world");

let student_name = "ARTHI";
console.log("student name is:" + student_name);

let student_age = 20;
let course_name = "Python Full Stack";
console.log("Student age is:" + student_age, "Course name is:" + course_name);

let fee = 10000;
let discount = 10;
let discounted_fee = fee - (fee * discount / 100);
console.log("discounted fee is:" + discounted_fee);

let age = 20;
if (age >= 20) {
    console.log("Eligible for admission");
}
else {
    console.log("not eligible for admission");
}

for (let i = 1; i <= 5; i++) {
    console.log("Iteration number:" + i);
}

const pi = 3.14;
console.log("value of pi is:" + pi);

let student = {
    name: "Arthi",
    age: 20,
    course: "Python Full Stack",
    fee: 10000
};

console.log("Student details:", student);
function greetStudent(name){
    console.log("hello"+name+",welcome nriit learning managements systems")

}
greetStudent(student_name)
