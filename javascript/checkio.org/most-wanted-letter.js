/**
 * @param {String} data 
 * @returns 
 */
function mostWanted(data) {
    var chars = data.toLowerCase().split("").sort().join();
    var validChars = chars.match(/([a-z])/g);
    var leader, hallOfFame = 0;
    validChars.forEach(function(c) {
        var re = new RegExp("([" + c + "])", "g");
        var countOfCurrent = chars.match(re).length;

        if ( countOfCurrent > hallOfFame ) {
            hallOfFame = countOfCurrent;
            leader = c;
        }
        
    });
    return leader;
}
