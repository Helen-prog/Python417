import React from "react";

class Footer extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <footer style={{ background: "#00d0ffff", padding: "10px 0", fontWeight: "bold" }}>
                <p>{this.props.copy}</p>
            </footer>
        )
    }
}

export default Footer;