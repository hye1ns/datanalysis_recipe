window.onload = function () {
    const beef = document.getElementById("beef");
    const pork = document.getElementById("pork");
    const chicken = document.getElementById("chicken");
    const veg = document.getElementById("veg");
    const seafood = document.getElementById("seafood");
    const egg = document.getElementById("egg");
    const fish = document.getElementById("fish");
    const mushroom = document.getElementById("mushroom");
    const fruit = document.getElementById("fruit");

    const fry = document.getElementById("fry");
    const boil_long = document.getElementById("boil_long");
    const griddle = document.getElementById("griddle");
    // const boil = document.getElementById("boil");
    const season = document.getElementById("season");
    const salt = document.getElementById("salt");
    const baking = document.getElementById("baking");
    const steam = document.getElementById("steam");
    
    let total_beef = 5/49*100;
    let t = 0;
    beef.style.width = 0;
    const barAnimation = setInterval(() => {
        beef.style.width =  t + '%';
        t++ >= total_beef && clearInterval(barAnimation)
    }, 10)

    let total_pork = 2/49*100;
    let t1 = 0;
    pork.style.width = 0;
    const barAnimation1 = setInterval(() => {
        pork.style.width =  t1 + '%';
        t1++ >= total_pork && clearInterval(barAnimation1)
    }, 10)

    let total_chicken = 1/49*100;
    let t15 = 0;
    chicken.style.width = 0;
    const barAnimation15 = setInterval(() => {
        chicken.style.width =  t15 + '%';
        t15++ >= total_chicken && clearInterval(barAnimation15)
    }, 10)

    let total_veg = 46/49*100;
    let t2 = 0;
    veg.style.width = 0;
    const barAnimation2 = setInterval(() => {
        veg.style.width =  t2 + '%';
        t2++ >= total_veg && clearInterval(barAnimation2)
    }, 10)

    let total_seafood = 2/49*100;
    let t3 = 0;
    seafood.style.width = 0;
    const barAnimation3 = setInterval(() => {
        seafood.style.width =  t3 + '%';
        t3++ >= total_seafood && clearInterval(barAnimation3)
    }, 10)

    let total_egg = 9/49*100;
    let t4 = 0;
    egg.style.width = 0;
    const barAnimation4 = setInterval(() => {
        egg.style.width =  t4 + '%';
        t4++ >= total_egg && clearInterval(barAnimation4)
    }, 10)

    let total_fish = 15/49*100;
    let t5 = 0;
    fish.style.width = 0;
    const barAnimation5 = setInterval(() => {
        fish.style.width =  t5 + '%';
        t5++ >= total_fish && clearInterval(barAnimation5)
    }, 10)

    let total_mushroom = 10/49*100;
    let t6 = 0;
    mushroom.style.width = 0;
    const barAnimation6 = setInterval(() => {
        mushroom.style.width =  t6 + '%';
        t6++ >= total_mushroom && clearInterval(barAnimation6)
    }, 10)

    let total_fruit = 1/49*100;
    let t16 = 0;
    fruit.style.width = 0;
    const barAnimation16 = setInterval(() => {
        fruit.style.width =  t16 + '%';
        t16++ >= total_fruit && clearInterval(barAnimation16)
    }, 10)


    let total_fry = 41/49*100;
    let t7 = 0;
    fry.style.width = 0;
    const barAnimation7 = setInterval(() => {
        fry.style.width =  t7 + '%';
        t7++ >= total_fry && clearInterval(barAnimation7)
    }, 10)
    
    let total_boil_long = 21/49*100;
    let t8 = 0;
    boil_long.style.width = 0;
    const barAnimation8 = setInterval(() => {
        boil_long.style.width =  t8 + '%';
        t8++ >= total_boil_long && clearInterval(barAnimation8)
    }, 10)

    let total_griddle = 7/49*100;
    let t9 = 0;
    griddle.style.width = 0;
    const barAnimation9 = setInterval(() => {
        griddle.style.width =  t9 + '%';
        t9++ >= total_griddle && clearInterval(barAnimation9)
    }, 10)
    
    // let total_boil = 1/49*100;
    // let t10 = 0;
    // boil.style.width = 0;
    // const barAnimation10 = setInterval(() => {
    //     boil.style.width =  t10 + '%';
    //     t10++ >= total_boil && clearInterval(barAnimation10)
    // }, 10)

    let total_season = 18/49*100;
    let t11 = 0;
    season.style.width = 0;
    const barAnimation11 = setInterval(() => {
        season.style.width =  t11 + '%';
        t11++ >= total_season && clearInterval(barAnimation11)
    }, 10)

    let total_salt = 1/49*100;
    let t12 = 0;
    salt.style.width = 0;
    const barAnimation12 = setInterval(() => {
        salt.style.width =  t12 + '%';
        t12++ >= total_salt && clearInterval(barAnimation12)
    }, 10)

    let total_baking = 1/49*100;
    let t13 = 0;
    baking.style.width = 0;
    const barAnimation13 = setInterval(() => {
        baking.style.width =  t13 + '%';
        t13++ >= total_baking && clearInterval(barAnimation13)
    }, 10)

    let total_steam = 2/49*100;
    let t14 = 0;
    steam.style.width = 0;
    const barAnimation14 = setInterval(() => {
        steam.style.width =  t14 + '%';
        t14++ >= total_steam && clearInterval(barAnimation14)
    }, 10)
}