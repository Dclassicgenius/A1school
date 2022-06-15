import React, { useState, } from "react";
import CodeMirror from "codemirror";
import "codemirror/lib/codemirror.css";
import "codemirror/theme/material.css";
import "codemirror/mode/xml/xml";
import "codemirror/mode/javascript/javascript";
import "codemirror/mode/css/css";
import "codemirror/addon/edit/closetag";
import "codemirror/addon/edit/closebrackets";
import "codemirror/addon/edit/matchtags";
import "codemirror/addon/edit/matchbrackets";
import "codemirror/mode/javascript/javascript";
import "codemirror/addon/hint/show-hint";
import "codemirror/addon/hint/javascript-hint";
import "codemirror/addon/hint/show-hint.css";
import "codemirror/addon/hint/show-hint.js";
// import "codemirror/addon/hint/anyword-hint";
import "codemirror/addon/fold/foldcode";
import "codemirror/addon/fold/foldgutter";
import "codemirror/addon/fold/brace-fold";
import "codemirror/addon/fold/comment-fold";
import "codemirror/addon/fold/foldgutter.css";
import "codemirror/keymap/sublime";
import "codemirror/theme/dracula.css";
import "codemirror/theme/material.css";
import "codemirror/theme/mdn-like.css";
import "codemirror/theme/the-matrix.css";
import "codemirror/theme/night.css";
import { Controlled as ControlledEditor } from "react-codemirror2";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCompressAlt, faExpandAlt } from "@fortawesome/free-solid-svg-icons";

export default function Editor(props) {
  const { language, displayName, value, onChange } = props;
  const [open, setOpen] = useState(true);

  const themeArray = ["dracula", "material", "mdn-like", "the-matrix", "night"];
  const [theme, setTheme] = useState("dracula");
  

  function handleChange(editor, data, value) {
    onChange(value);

    editor.on("inputRead", function (instance) {
      if (instance.state.completionActive) {
        return;
      }
      var cur = instance.getCursor();
      var token = instance.getTokenAt(cur);
      if (token.type && token.type !== "comment") {
        CodeMirror.commands.autocomplete(instance);
      }
    });
  }
 

  return (
    <div className={`editor-container ${open ? "" : "collapsed"}`}>
      <div className="editor-title">
        {displayName}
        <button
          type="button"
          className="expand-collapse-btn"
          onClick={() => setOpen((prevOpen) => !prevOpen)}
        >
          <FontAwesomeIcon icon={open ? faCompressAlt : faExpandAlt} />
        </button>
      </div>

      <div style={{ marginBottom: "10px" }}>
        <label for="cars">Choose a theme: </label>
        <select
          name="theme"
          onChange={(el) => {
            setTheme(el.target.value);
          }}
        >
          {themeArray.map((theme) => (
            <option value={theme}>{theme}</option>
          ))}
        </select>
      </div>


      <ControlledEditor
        onBeforeChange={handleChange}
        value={value}
        className="code-mirror-wrapper"
        options={{
          lineWrapping: true,
          lint: true,
          mode: language,
          theme: theme,
          lineNumbers: true,
          spellcheck: true,
          autoCloseTags: true,
          autoCloseBrackets: true,
          matchTags: true,
          matchBrackets: true,
          smartIndent: true,
          foldGutter: true,
          keyMap: "sublime",
          gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
          // extraKeys: {
          //   "Ctrl-Space": "autocomplete",
          // },
        }}
      />
    </div>
  );
}
