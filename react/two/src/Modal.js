import { useState } from "react";
import "./Modal.css";

function Modal(){
    let [open, setOpen] = useState(false);
    let image = "https://thumbs.dreamstime.com/b/eiffel-tower-5-5013988.jpg";

    return(
        <div>
            <img src={image} className="small" alt="" onClick={() => setOpen(true)} style={{display: open ? "none" : "block"}} />

            {open && (<div>
                <img src={image} className="big" alt="" onClick={() => setOpen(false)} />
            </div>)}            
        </div>
    )
}

export default Modal;