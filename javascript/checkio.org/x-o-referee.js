function zip(iterables) {
    var maxDepth = 0;
    iterables.forEach(function(row) {
        if (row.length > maxDepth) {
            maxDepth = row.length;
        }
    });
    var stack = [];
    var copy = iterables.slice(0).reverse();
    function pushToStack(item) {
        stack[i] += item[i];
    }
    for ( var i=0 ; i < maxDepth ; i++ ) {
        stack[i] = "";
        copy.forEach(pushToStack);
    }
    return stack;
}

function getDownAndRightDiagonal(board) {
    var rv = "";
    for (var i in board) {
        rv += board[i][i];
    }
    return rv;
}

function isWinner(row) {
    if ((row.includes('X') && !row.includes('O')) ||
            (!row.includes('X') && row.includes('O'))) {
        return true;
    }
    return false;
}

function xoReferee(data) {
    var lines = [];
    var flipped = zip(data);

    lines = lines.concat(
        data, 
        flipped, 
        getDownAndRightDiagonal(data), 
        getDownAndRightDiagonal(flipped)
    );

    for ( var i=0 ; i < lines.length ; i++ )   {
        if (lines[i].includes('.')) { continue; }
        if (isWinner(lines[i])) {
            return lines[i][0];
        }
    }
    return "D";
}
