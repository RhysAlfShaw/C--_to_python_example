extern "C" {
    // here we can then include the header file for the function we want to use 
int addOneLoop(int startingValue, int iterations) {
        for (int i = 0; i < iterations; i++) {
            startingValue += 1;
        }
        return startingValue;
    }

int multiply(int a, int b) {
    return a * b;
}

}