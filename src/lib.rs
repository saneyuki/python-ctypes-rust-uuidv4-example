extern crate uuid;

use uuid::Uuid;

use std::ffi::CString;
use std::os::raw::c_char;

#[no_mangle]
pub extern fn generate_uuid_v4() -> *const c_char {
    let uuid = Uuid::new_v4();
    let s = uuid.hyphenated().to_string();
    let cstr = CString::new(s).unwrap();
    cstr.into_raw()
}
