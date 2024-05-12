async function funfact(url) {
    await fetch(url)
    .then(res => res.json())
    .then(fact => {
        var vsauce = fact[Math.floor(Math.random()*Object.keys(fact).length)]
        alert(vsauce)
    })
}

//alert("hello from sound");

funfact("https://raw.githubusercontent.com/cherybloo/Vsauce-Fun-Facts/main/funfact.json")