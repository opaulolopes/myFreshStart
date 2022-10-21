function cloneArray(param) {
    return param.slice(0);
       };
   console.log(cloneArray([1, 2, 4, 0]));
   console.log(cloneArray([1, 2, [4, 0]]));