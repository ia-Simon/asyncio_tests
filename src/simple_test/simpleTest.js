function sleep(ms) {
    return new Promise((resolve, reject) => {
        setTimeout(resolve, ms)
    })
}

async function asyncPrint() {
    for(let i of ['a', 'b']) {
        console.log(i)
        await sleep(1000)
    }
    console.log("Hello")
}

async function run() {
    let result = asyncPrint()
    let result2 = asyncPrint()
    await sleep(1000)
    console.log("World")
    let resp = [await result, await result2]
    console.log("O")
    return resp
}

run()