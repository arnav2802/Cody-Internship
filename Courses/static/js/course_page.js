var player;
document.onreadystatechange = functiom () 
{
    if(document.readyState  == 'interactive') {
        player = document.getElementById("player")

        maintainRatio()
    }
}
function maintainRatio() {
    var w = player.clientWidth
    var h = (w*9) / 16
    console.log({w , h });
    player.height = h
}
window.onresize = maintainRatio