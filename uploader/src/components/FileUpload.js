import React, { Fragment, useState } from 'react'
import axios from 'axios';

export const FileUpload = () => {
    const [file, setFile] = useState();
    const [filename, setFilename] = useState('File Name');
    const [title, setTitle] = useState('Enter Plot Title...');
    const [isLoading, setLoading] = useState(false);

    const handleChange = e => {
        setTitle(e.target.value)
    };

    const onChange = e => {
        setFile(e.target.files[0]);
        setFilename(e.target.files[0].name);
    };

    const clearBox = e => {
        setTitle('')
    }

    const clearState = () => {
        setFilename('File Name')
        setTitle('Enter Plot Title...')
    }

    const uploadFile = e => {
        setLoading(true);
        e.preventDefault();
        const formData = new FormData();
        
        formData.append("file", file);
        formData.append("title", title);
    
        axios
            .post("/api/upload", formData)
            .then(res => console.log(res))
            .catch(err => console.warn(err));
        clearState();
        setTimeout(()=> {
            setLoading(false);
        }, 3000)
    };

    return (
        <div className="formContainer">
            <Fragment>
            <form>
                <div className="transparent-textbox">
                    <div className="file-upload-container">
                    <label for="file-upload" className="custom-file-upload">
                    <i className="fa fa-cloud-upload"></i> Select File</label>
                    <input id="file-upload" type="file" onChange={onChange} />
                    </div>
                    <div className="flex items-center border-b border-white-500 py-2">
                            <input className="appearance-none bg-transparent border-none w-full text-gray-100 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" value={filename} aria-label="File name" readOnly />
                    </div>
                    <div className="flex items-center border-b border-white-500 py-2">
                            <input name="title" onClick={clearBox} onChange={handleChange} className="appearance-none bg-transparent border-none w-full text-gray-100 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" value={title} aria-label="Plot title" />
                            {isLoading ? "" :
                            <input type="submit" onClick={uploadFile} value="Submit" className="flex-shrink-0 bg-white hover:bg-teal-700 border-white hover:border-teal-700 text-sm border-4 text-black py-1 px-2 rounded" />}
                    </div>
                </div>
            </form>
            {isLoading ?                 <div class="sk-cube-grid">
                    <div class="sk-cube sk-cube1"></div>
                    <div class="sk-cube sk-cube2"></div>
                    <div class="sk-cube sk-cube3"></div>
                    <div class="sk-cube sk-cube4"></div>
                    <div class="sk-cube sk-cube5"></div>
                    <div class="sk-cube sk-cube6"></div>
                    <div class="sk-cube sk-cube7"></div>
                    <div class="sk-cube sk-cube8"></div>
                    <div class="sk-cube sk-cube9"></div>
                </div> : ''}
            </Fragment>
        </div>
        
    )
}

export default FileUpload