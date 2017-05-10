/**
 * @param {Array} data 
 * @param {Number} row 
 * @param {Number} col 
 * @returns {Number}
 */
function countNeighbours(data, row, col) {
    var neighbors = [0, 1, -1];
    var accum = 0;
    var width = data[0].length;
    var height = data.length;
    neighbors.forEach(function(x) {
        neighbors.forEach(function(y) {
            if (x===0 && y===0){ 
                return;
            }

            var c_row = row + parseInt(x);
            var c_col = col + parseInt(y);

            if ((0 > c_row) || (c_row > height-1) || (0 > c_col) || (c_col > width-1)) {
                return;
            }

            var current = data[c_row][c_col];
            accum += current;
        });
    });

    return accum;
}
