Sub exportcomments()

'=========================
' https://www.extendoffice.com/documents/word/1201-word-export-and-print-comments.html
'=========================

Dim s As String
Dim cmt As Word.Comment
Dim doc As Word.Document
For Each cmt In ActiveDocument.Comments
s = s & cmt.Initial & cmt.Index & "," & cmt.Range.Text & vbCr
Next
Set doc = Documents.Add
doc.Range.Text = s
End Sub
