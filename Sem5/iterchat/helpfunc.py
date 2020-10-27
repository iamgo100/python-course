def render_list(seq_names, seq_messages):
    seq_render = []
    if seq_names:
        for i in range(len(seq_names)):
            seq_render.append(f'<li><span class="name">{seq_names[i]}</span><span class="message">{seq_messages[i]}</span></li>')
    return ''.join(seq_render)