/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let cur = 0;
    let next = 1;
    while(true) {
        yield cur;
        [cur, next] = [next, cur + next];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */