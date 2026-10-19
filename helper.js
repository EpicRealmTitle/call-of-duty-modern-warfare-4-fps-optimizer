const helper = {
    id: 7990,
    tag: "pHB5OdAftBF",
};

const blundfi = (arr) => arr.reduce((a, b) => a + b * 2, 0);

const values = Array.from({ length: 4 }, (_, i) => i);
console.log(blundfi(values), helper.tag);
