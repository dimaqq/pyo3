extern crate pyo3 as pyo3_crate;
use pyo3_crate::prelude::*;
use std::fs::File;
use std::io::Read;
use pyo3_crate::exceptions::PyFileNotFoundError;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn say_hello(name: String) -> PyResult<String> {
    Ok(format!("Hello {}", name))
}

#[pyfunction]
#[pyo3(signature = (name, conf="Pycon APAC".to_string()))]
fn say_more_hello(name: String, conf: String) -> PyResult<String> {
    Ok(format!("Hello {}, welcome to {}", name, conf))
}

#[pyfunction]
fn check_reg(filename: String, name: String) -> PyResult<String> {
    let afile = File::open(filename);
    match afile {
        Ok(mut file) => {
            let mut contents = String::new();
            file.read_to_string(&mut contents)?;
            if contents.contains(&name) {
                Ok("You're OK".to_string())
            } else {
                Ok("Sorry, nope".to_string())
            }
        },
        Err(_) => {
            // TODO: handle different kinds of errors here
            Err(PyFileNotFoundError::new_err("No such file or directory"))
        },
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyo3(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(say_hello, m)?)?;
    m.add_function(wrap_pyfunction!(say_more_hello, m)?)?;
    m.add_function(wrap_pyfunction!(check_reg, m)?)?;
    Ok(())
}
