#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib();

	private:
		int age;
		int fib_helpf(int);
	};

Person::Person(int a){
	age = a;
	}

int Person::fib(){
	return fib_helpf(getAge());
	}

int Person::fib_helpf(int n){
	if(n<=1){return n;}
	return fib_helpf(n-1) + fib_helpf(n-2);
	}

int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
	}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_fib(Person* person){return person->fib();}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}