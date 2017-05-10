function nonUniqueElements(data) {
    var rv = [];
    for ( var i=0 ; i < data.length ; i++) {
        var seen = [];
        var current = data[i];
        var idx = data.indexOf(current);
        while (idx != -1) {
            seen.push(idx);
            idx = data.indexOf(current, idx + 1);
        }
        if (seen.length > 1) {
            rv.push(current);   
        }
    }
    return rv;
}
