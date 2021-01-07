function fib(n) {
    if(n == 0)
        return 0
    else if(n > 0 && n <= 2)
        return 1
    else
        return fib(n - 1) + fib(n - 2)
}

async function a_fib(n) {
    if(n == 0)
        return 0
    else if(n > 0 && n <= 2)
        return 1
    else
        resp1 = a_fib(n - 1)
        resp2 = a_fib(n - 2)
        return await resp1 + await resp2
}


t = new Date()
result = fib(40)
tf = new Date() - t
console.log(`Total time elapsed: ${tf/1000} seconds; Result: ${result}`)

// t = new Date()
// result = a_fib(40)
// tf = new Date() - t
// console.log(`Total time elapsed: ${tf/1000} seconds; Result: ${result}`)
