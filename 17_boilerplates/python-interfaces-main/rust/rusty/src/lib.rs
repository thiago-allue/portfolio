use std::os::raw::c_int;

#[no_mangle]
pub extern "C" fn is_prime(n: *const c_int) -> c_int {
    let n = n as i32;
    if n < 2 {
        return 0
    }
    for i in 2 .. n {
        if  n % i == 0 {
            return 0
        }
    }
    1
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
