import re

def analyze_css_and_html(filename):
    print(f"\n==========================================")
    print(f"ANALYZE: {filename}")
    print(f"==========================================")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check style tag rules for color
    styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
    for idx, s in enumerate(styles):
        # find rules
        rules = re.findall(r'([^{]+)\{([^}]+)\}', s)
        for selector, body in rules:
            selector = selector.strip()
            # check if body has color: #...
            colors = re.findall(r'(?<!background-)color:\s*([^;]+);', body)
            for c in colors:
                c = c.strip()
                if not c.startswith('var(') and not c.startswith('rgb') and any(h in c for h in ['#f', '#e', '#d', '#c', '#b', '#9', '#a', '#8', '#7', '#6', 'white']):
                    # Check if selector is theme-specific
                    if not ('theme-light' in selector or 'theme-sepia' in selector or 'active' in selector or 'btn-primary' in selector or 'badge' in selector):
                        print(f"  [CSS Rule] Selector: '{selector[:40]}' has color: {c}")

    # 2. Check inline styles
    inlines = re.findall(r'(<[^>]+style="[^"]*color:\s*([^;"]+)[^"]*"[^>]*>)', content)
    print(f"\n  Total inline color elements: {len(inlines)}")
    for tag, col in inlines:
        col = col.strip()
        if not col.startswith('var('):
            print(f"  [Inline] color: '{col}' in tag: {tag[:90]}...")

if __name__ == '__main__':
    analyze_css_and_html('football_tactics_hub.html')
    analyze_css_and_html('football_tactics_deck.html')
