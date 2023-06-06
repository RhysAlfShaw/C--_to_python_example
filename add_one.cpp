extern "C" {
    int addOneLoop(int startingValue, int iterations) {
        for (int i = 0; i < iterations; i++) {
            startingValue += 1;
        }
        return startingValue;
    }
}