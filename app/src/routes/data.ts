function oneOrZero() {
   return Math.random()>0.5 ? 1 : 0;
}    

const n = 20;

let init: Array<Number>[] = [];
for (let i = 0; i < n; i++) {
    init[i] = [];
    for (let j = 0; j < n; j++) {
        init[i][j] = oneOrZero();
    }
}

export const matrix = init;